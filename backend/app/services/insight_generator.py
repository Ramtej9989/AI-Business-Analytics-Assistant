def generate_ai_insights(
    dataframe,
    column_types,
    data_quality,
    eda_analysis,
    correlation_analysis,
) -> dict:
    rows = dataframe.shape[0]
    columns = dataframe.shape[1]

    quality_score = data_quality.get("quality_score", 0)

    executive_summary = (
        f"The dataset contains {rows:,} records across "
        f"{columns} columns with an overall data quality "
        f"score of {quality_score}%. "
        "The analysis identified important statistical patterns, "
        "data quality risks, and potential business opportunities."
    )

    key_findings = []

    numerical_columns = column_types.get("numerical", [])

    if numerical_columns:
        key_findings.append(
            f"The dataset contains {len(numerical_columns)} "
            "numerical features suitable for statistical "
            "and trend analysis."
        )

    categorical_columns = column_types.get("categorical", [])

    if categorical_columns:
        key_findings.append(
            f"{len(categorical_columns)} categorical features "
            "can be used for customer segmentation and "
            "group-based business analysis."
        )

    strong_correlations = correlation_analysis.get(
        "strong_correlations",
        []
    )

    if strong_correlations:
        key_findings.append(
            f"{len(strong_correlations)} strong relationships "
            "were detected between numerical variables."
        )

    if not key_findings:
        key_findings.append(
            "The dataset is suitable for exploratory "
            "business analysis."
        )

    business_risks = []

    missing_values = int(dataframe.isnull().sum().sum())

    if missing_values > 0:
        business_risks.append(
            f"{missing_values:,} missing values may affect "
            "analysis accuracy and machine learning results."
        )

    duplicate_rows = int(dataframe.duplicated().sum())

    if duplicate_rows > 0:
        business_risks.append(
            f"{duplicate_rows:,} duplicate records may create "
            "biased business metrics."
        )

    if quality_score < 80:
        business_risks.append(
            "The dataset has a low data quality score and "
            "should be cleaned before advanced analysis."
        )

    if not business_risks:
        business_risks.append(
            "No major data quality risks were detected."
        )

    opportunities = []

    if categorical_columns:
        opportunities.append(
            "Use categorical features to identify customer "
            "segments and compare business performance."
        )

    if numerical_columns:
        opportunities.append(
            "Analyze numerical trends to identify high-value "
            "customers and important performance drivers."
        )

    if strong_correlations:
        opportunities.append(
            "Use strongly correlated variables to support "
            "predictive modeling and business forecasting."
        )

    opportunities.append(
        "The dataset can be used to build automated dashboards "
        "and machine learning models for decision support."
    )

    return {
        "executive_summary": executive_summary,
        "key_findings": key_findings,
        "business_risks": business_risks,
        "opportunities": opportunities,
    }