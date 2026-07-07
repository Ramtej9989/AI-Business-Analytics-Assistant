import pandas as pd


class DatasetStore:
    """
    Temporary in-memory storage for the currently uploaded dataset.
    """

    def __init__(self):
        self._dataframe: pd.DataFrame | None = None
        self._filename: str | None = None
        self._dataset_id: int | None = None

    def save_dataset(
        self,
        dataframe: pd.DataFrame,
        filename: str,
        dataset_id: int,
    ) -> None:
        """
        Store the uploaded dataset and its database ID in memory.
        """

        self._dataframe = dataframe.copy()
        self._filename = filename
        self._dataset_id = dataset_id

    def get_dataset(self) -> pd.DataFrame | None:
        """
        Return the currently stored dataset.
        """

        if self._dataframe is None:
            return None

        return self._dataframe.copy()

    def get_filename(self) -> str | None:
        """
        Return the uploaded dataset filename.
        """

        return self._filename

    def get_dataset_id(self) -> int | None:
        """
        Return the database ID of the currently stored dataset.
        """

        return self._dataset_id

    def has_dataset(self) -> bool:
        """
        Check whether a dataset is currently stored.
        """

        return self._dataframe is not None

    def clear_dataset(self) -> None:
        """
        Remove the currently stored dataset.
        """

        self._dataframe = None
        self._filename = None
        self._dataset_id = None


dataset_store = DatasetStore()