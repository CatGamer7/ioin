from django.conf import settings
import numpy as np
import onnxruntime as ort
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from transformers import AutoTokenizer

from inference.models import Message
from .serializers import MessageSerializer


sess = ort.InferenceSession(
    settings.BASE_DIR / "api/file/naive_bert_classifier.onnx"
)
tokenizer = AutoTokenizer.from_pretrained(
    settings.BASE_DIR / "api/file/naive_bert_tokenizer"
)


class ClassifyText(APIView):
    def post(self, request):
        text = request.data.get("text", None)
        chat_id = request.data.get("chat_id", None)

        if not text or not chat_id:
            return Response(
                {"error": "Missing 'text' or 'chat_id'"},
                status=status.HTTP_400_BAD_REQUEST
            )

        inputs = tokenizer(
            text,
            return_tensors="np",
            truncation=True,
            padding="max_length",
            max_length=512,
        )

        logits = sess.run(
            None,
            {
                "input_ids": inputs["input_ids"],
                "attention_mask": inputs["attention_mask"],
                "token_type_ids": inputs["token_type_ids"],
            },
        )[0]

        probs = np.exp(logits) / np.sum(np.exp(logits), axis=-1, keepdims=True)
        class_0_prob, class_1_prob, class_2_prob = probs[0]

        message = Message.objects.create(
            chat_id=chat_id,
            text=text,
            class_0_probability=class_0_prob,
            class_1_probability=class_1_prob,
            class_2_probability=class_2_prob,
        )

        serializer = MessageSerializer(message)

        return Response(serializer.data)
