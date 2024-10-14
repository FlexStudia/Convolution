# coding: utf-8

"""
    This modul helps classes without an interface to return a progress dialogue to a parent with an interface.
"""

# PACKAGES
from PyQt5.QtWidgets import QProgressDialog
from PyQt5.QtCore import Qt


def initialize_progress_dialog(parent_window, max_duration, title="Calculating...", text='Processing', abort_text='Cancel'):
    """
        Initializes and shows a QProgressDialog.

        Creates a modal progress dialog with specified parameters, which can
        be used to provide feedback on the progress of foreground tasks
        and potentially allow users to abort the operation.

    :param parent_window: QWidget
        The parent window for the progress dialog.
    :param max_duration: int
        Maximum duration for the progress bar.
    :param title: str, optional
        The title of the progress dialog (default is "Calculating...").
    :param text: str, optional
        The text message displayed in the progress dialog (default is 'Processing').
    :param abort_text: str, optional
        The text displayed on the cancel button (default is 'Cancel').
    :return progress: QProgressDialog
        The initialized and shown QProgressDialog instance.
    """
    try:
        if parent_window:
            progress = QProgressDialog(text, abort_text, 0, max_duration, parent_window)
            progress.setWindowModality(Qt.WindowModality.WindowModal)
            progress.setStyleSheet("QLabel{min-width: 300px;}")
            progress.setMinimumDuration(0)
            progress.setWindowTitle(title)
            progress.show()
            return progress
    except Exception as e:
        print(f"Error in initialize_progress_dialog: {e}")


def update_progress(parent_window, progress, i):
    """
        Updates the progress of a given progress indicator.

        This function updates the progress value of a progress indicator
        associated with a parent window. It also checks if the progress
        was canceled, in which case, it returns False.

    :param parent_window: QWidget
    	The parent window for the progress dialog.
    :param progress: QProgressBar
        The progress bar whose value needs to be updated.
    :param i: int
        The current progress value to set on the progress bar.
    :return: bool
        Returns True if the progress was successfully updated and not canceled,
        otherwise returns False.
    """
    try:
        if parent_window:
            progress.setValue(i)
            if progress.wasCanceled():
                return False
        return True
    except Exception as e:
        print(f"Error in update_progress: {e}")


def finalize_progress(parent_window, progress, max_duration):
    """
        Finalize the progress by setting it to the maximum duration and closing.

        This function sets the progress value to the specified maximum duration and closes the progress window.

    :param parent_window: QWidget
    	The parent window for the progress dialog.
    :param progress: QProgressDialog
        The progress dialog instance that needs to be finalized.
    :param max_duration: int
        The maximum value to set for the progress.

    :return: None
        The function returns nothing, but updates the progress dialog and may close it.
    """
    try:
        if parent_window:
            progress.setValue(max_duration)
            progress.close()
    except Exception as e:
        print(f"Error in finalize_progress: {e}")
