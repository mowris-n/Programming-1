import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._label1.Location = System.Drawing.Point(76, 59)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(178, 36)
        self._label1.TabIndex = 0
        self._label1.Text = "Radius"
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._label2.Location = System.Drawing.Point(76, 120)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(178, 36)
        self._label2.TabIndex = 1
        self._label2.Text = "Area"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._label3.Location = System.Drawing.Point(76, 183)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(178, 36)
        self._label3.TabIndex = 2
        self._label3.Text = "Circumference"
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._label4.Location = System.Drawing.Point(331, 183)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(178, 36)
        self._label4.TabIndex = 3
        self._label4.Text = "label4"
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._label5.Location = System.Drawing.Point(331, 120)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(178, 36)
        self._label5.TabIndex = 4
        self._label5.Text = "label5"
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._label6.Location = System.Drawing.Point(331, 59)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(178, 36)
        self._label6.TabIndex = 5
        self._label6.Text = "label6"
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(934, 407)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "prog54c"
        self.ResumeLayout(False)

