export default function DataQuality({ analysisData }) {
  const dataset = analysisData.dataset;
  const dataQuality = dataset.data_quality;
  const recommendations =
    dataset.cleaning_recommendations || [];

  const getRecommendationTitle = (recommendation) => {
    if (recommendation.issue === "duplicate_rows") {
      return "Duplicate Rows";
    }

    if (recommendation.issue === "constant_column") {
      return recommendation.column || "Constant Column";
    }

    return recommendation.column || "Dataset";
  };

  const getRecommendationMetric = (recommendation) => {
    if (
      recommendation.issue === "missing_values" ||
      recommendation.issue === "high_missing_values"
    ) {
      return `${recommendation.missing_percentage}% missing`;
    }

    if (recommendation.issue === "duplicate_rows") {
      return `${recommendation.duplicate_count} duplicate rows`;
    }

    if (recommendation.issue === "constant_column") {
      const uniqueCount =
        recommendation.unique_count ?? 1;

      return `${uniqueCount} unique value${
        uniqueCount === 1 ? "" : "s"
      }`;
    }

    return "Review recommended";
  };

  return (
    <section className="dashboard-section">
      <div className="section-header">
        <div>
          <h2>Data Quality</h2>

          <p>
            Dataset health, missing values, and cleaning
            recommendations.
          </p>
        </div>

        <div className="quality-score">
          <span>Quality Score</span>

          <strong>
            {dataQuality.quality_score}%
          </strong>
        </div>
      </div>

      <div className="quality-grid">
        <div className="quality-card">
          <p>Total Missing Values</p>

          <h3>
            {dataQuality.total_missing_values.toLocaleString()}
          </h3>

          <span>
            {dataQuality.missing_percentage}% of dataset
          </span>
        </div>

        <div className="quality-card">
          <p>Duplicate Rows</p>

          <h3>
            {dataQuality.duplicate_rows.toLocaleString()}
          </h3>

          <span>Duplicate records detected</span>
        </div>

        <div className="quality-card">
          <p>Duplicate Columns</p>

          <h3>
            {dataQuality.duplicate_columns.length}
          </h3>

          <span>Duplicate columns detected</span>
        </div>

        <div className="quality-card">
          <p>Constant Columns</p>

          <h3>
            {dataQuality.constant_columns.length}
          </h3>

          <span>Columns with one unique value</span>
        </div>
      </div>

      <div className="recommendations-card">
        <h3>Cleaning Recommendations</h3>

        {recommendations.length === 0 ? (
          <p className="empty-message">
            No cleaning recommendations found.
          </p>
        ) : (
          <div className="recommendations-list">
            {recommendations.map(
              (recommendation, index) => (
                <div
                  className="recommendation-item"
                  key={`${
                    recommendation.issue
                  }-${
                    recommendation.column || "dataset"
                  }-${index}`}
                >
                  <div>
                    <strong>
                      {getRecommendationTitle(
                        recommendation
                      )}
                    </strong>

                    <p>
                      {recommendation.recommendation}
                    </p>
                  </div>

                  <span>
                    {getRecommendationMetric(
                      recommendation
                    )}
                  </span>
                </div>
              )
            )}
          </div>
        )}
      </div>
    </section>
  );
}