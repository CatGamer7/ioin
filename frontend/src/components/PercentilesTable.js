function PercentilesTable({ percentiles }) {
  return (
    <div className="table-responsive mb-4">
      <table className="table table-bordered">
        <thead>
          <tr>
            <th>Percentile</th>
            <th>Class 0</th>
            <th>Class 1</th>
            <th>Class 2</th>
          </tr>
        </thead>
        <tbody>
          {[1, 25, 50, 75, 99].map((percentile, index) => (
            <tr key={percentile}>
              <td>{percentile}%</td>
              <td>{percentiles.class_0_percentiles[index]}</td>
              <td>{percentiles.class_1_percentiles[index]}</td>
              <td>{percentiles.class_2_percentiles[index]}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default PercentilesTable;
