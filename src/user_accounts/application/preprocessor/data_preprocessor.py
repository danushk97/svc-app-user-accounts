"""
This modules hols the DataPreprocessor class.
"""

class DataPreprocessor:
    """
    Holds the helper function to preprocess the data before inserting into the
    database.
    """
    @staticmethod
    def strip_and_lower(value: str) -> str:
        """
        Strips and lower the value.

        Args:
            value (str): Any string value.

        Returns:
            value (str)

        example:
            >>>strip_and_lower('String VAlue  ')
            'string value'
            >>>strip_and_lower('String Value')
            'string value'
            >>>
        """
        return value.strip().lower()
