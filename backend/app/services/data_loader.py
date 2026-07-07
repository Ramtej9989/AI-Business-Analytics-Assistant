from io import BytesIO

import pandas as pd
from fastapi import HTTPException, UploadFile


async def load_dataset(file: UploadFile) -> pd.DataFrame:
    filename = file.filename

    if not filename:
        raise HTTPException(
            status_code=400,
            detail="File name is missing"
        )

    file_extension = filename.lower().split(".")[-1]

    if file_extension not in ["csv", "xlsx"]:
        raise HTTPException(
            status_code=400,
            detail="Only CSV and Excel (.xlsx) files are supported"
        )

    file_content = await file.read()

    if not file_content:
        raise HTTPException(
            status_code=400,
            detail="Uploaded file is empty"
        )

    try:
        if file_extension == "csv":
            dataframe = pd.read_csv(BytesIO(file_content))

        else:
            dataframe = pd.read_excel(BytesIO(file_content))

    except Exception as error:
        raise HTTPException(
            status_code=400,
            detail=f"Unable to read dataset: {str(error)}"
        )

    if dataframe.empty:
        raise HTTPException(
            status_code=400,
            detail="Dataset contains no data"
        )

    return dataframe