"use client";

import {
  Bar,
  BarChart,
  CartesianGrid,
  ResponsiveContainer,
  Scatter,
  ScatterChart,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts";

export default function Charts({ analysisData }) {
  const charts = analysisData?.dataset?.chart_data || [];

  if (charts.length === 0) {
    return (
      <section className="dashboard-section">
        <div className="section-header">
          <div>
            <h2>Charts & Visualizations</h2>
            <p>
              Automatically generated visual analysis of your dataset.
            </p>
          </div>
        </div>

        <div className="charts-empty-card">
          <p className="empty-message">
            No chart data available for this dataset.
          </p>
        </div>
      </section>
    );
  }

  const renderChart = (chart) => {
    if (
      chart.chart_type === "bar" ||
      chart.chart_type === "histogram"
    ) {
      return (
        <ResponsiveContainer width="100%" height={300}>
          <BarChart
            data={chart.data}
            margin={{
              top: 10,
              right: 10,
              left: 0,
              bottom: 30,
            }}
          >
            <CartesianGrid
              strokeDasharray="3 3"
              stroke="#1e3a52"
            />

            <XAxis
              dataKey="label"
              stroke="#94a3b8"
              tick={{
                fill: "#94a3b8",
                fontSize: 11,
              }}
              angle={-25}
              textAnchor="end"
              interval={0}
            />

            <YAxis
              stroke="#94a3b8"
              tick={{
                fill: "#94a3b8",
                fontSize: 11,
              }}
            />

            <Tooltip
              contentStyle={{
                background: "#0d1b2a",
                border: "1px solid #1e3a52",
                borderRadius: "10px",
                color: "#f1f5f9",
              }}
              cursor={{
                fill: "rgba(6, 182, 212, 0.08)",
              }}
            />

            <Bar
              dataKey="value"
              fill="#06b6d4"
              radius={[6, 6, 0, 0]}
            />
          </BarChart>
        </ResponsiveContainer>
      );
    }

    if (chart.chart_type === "scatter") {
      return (
        <ResponsiveContainer width="100%" height={300}>
          <ScatterChart
            margin={{
              top: 10,
              right: 20,
              left: 0,
              bottom: 20,
            }}
          >
            <CartesianGrid
              strokeDasharray="3 3"
              stroke="#1e3a52"
            />

            <XAxis
              type="number"
              dataKey="x"
              name={chart.x_axis}
              stroke="#94a3b8"
              tick={{
                fill: "#94a3b8",
                fontSize: 11,
              }}
            />

            <YAxis
              type="number"
              dataKey="y"
              name={chart.y_axis}
              stroke="#94a3b8"
              tick={{
                fill: "#94a3b8",
                fontSize: 11,
              }}
            />

            <Tooltip
              cursor={{
                strokeDasharray: "3 3",
              }}
              contentStyle={{
                background: "#0d1b2a",
                border: "1px solid #1e3a52",
                borderRadius: "10px",
                color: "#f1f5f9",
              }}
            />

            <Scatter
              data={chart.data}
              fill="#22d3ee"
            />
          </ScatterChart>
        </ResponsiveContainer>
      );
    }

    return null;
  };

  return (
    <section className="dashboard-section">
      <div className="section-header">
        <div>
          <h2>Charts & Visualizations</h2>

          <p>
            Automatically recommended visualizations based on your data.
          </p>
        </div>

        <div className="chart-count">
          <span>Generated Charts</span>
          <strong>{charts.length}</strong>
        </div>
      </div>

      <div className="charts-grid">
        {charts.map((chart, index) => (
          <div
            className="chart-card"
            key={`${chart.title}-${index}`}
          >
            <div className="chart-card-header">
              <div>
                <h3>{chart.title}</h3>
                <p>{chart.reason}</p>
              </div>

              <span className="chart-type">
                {chart.chart_type}
              </span>
            </div>

            <div className="chart-wrapper">
              {renderChart(chart)}
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}
