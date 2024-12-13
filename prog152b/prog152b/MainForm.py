import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._listBox1 = System.Windows.Forms.ListBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.White
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 11)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(113, 31)
		self._label1.TabIndex = 0
		self._label1.Text = "Input:"
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(131, 11)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(126, 31)
		self._textBox1.TabIndex = 1
		# 
		# listBox1
		# 
		self._listBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._listBox1.FormattingEnabled = True
		self._listBox1.ItemHeight = 25
		self._listBox1.Location = System.Drawing.Point(13, 55)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(489, 254)
		self._listBox1.TabIndex = 2
		self._listBox1.SelectedIndexChanged += self.ListBox1SelectedIndexChanged
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(13, 315)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(119, 44)
		self._button1.TabIndex = 3
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(184, 316)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(119, 44)
		self._button2.TabIndex = 4
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(358, 316)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(119, 44)
		self._button3.TabIndex = 5
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.DarkSlateGray
		self.ClientSize = System.Drawing.Size(514, 372)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._listBox1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "prog152b"
		self.ResumeLayout(False)
		self.PerformLayout()


	def ListBox1SelectedIndexChanged(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		heading = "Even Integer:" + "\t\t" + "Sum:"
		self._listBox1.Items.Add(heading)
		while pass
		