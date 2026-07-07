export default function OverviewCards({ analysisData }) {
  const dataset = analysisData.dataset;
  const dataQuality = dataset.data_quality;

  const overviewCards = [
    {
      title: "Total Rows",
      value: dataset.rows.toLocaleString(),
      description: "Dataset records",
    },
    {
      title: "Total Columns",
      value: dataset.columns,
      description: "Dataset features",
    },
    {
      title: "Data Quality",
      value: `${dataQuality.quality_score}%`,
      description: "Overall quality score",
    },
    {
      title: "Missing Values",
      value: dataQuality.total_missing_values.toLocaleString(),
      description: `${dataQuality.missing_percentage}% missing`,
    },
  ];

  return (
    <section className="overview-grid">
      {overviewCards.map((card) => (
        <div className="overview-card" key={card.title}>
          <p>{card.title}</p>

          <h2>{card.value}</h2>

          <span>{card.description}</span>
        </div>
      ))}
    </section>
  );
}