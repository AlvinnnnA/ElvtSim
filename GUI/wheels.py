from PySide6.QtWidgets import QMessageBox, QTextEdit


class ElvtTeamEventPrompt(QMessageBox):

    # This is a much better way to extend __init__
    def __init__(self, *args, **kwargs):
        super(ElvtTeamEventPrompt, self).__init__(*args, **kwargs)
        # Anything else you want goes below

    # We only need to extend resizeEvent, not every event.
    def resizeEvent(self, event):

        result = super(ElvtTeamEventPrompt, self).resizeEvent(event)

        details_box = self.findChild(QTextEdit)
        # 'is not' is better style than '!=' for None
        if details_box is not None:
            details_box.setFixedSize(details_box.sizeHint())

        return result