import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._listBox1 = System.Windows.Forms.ListBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# listBox1
		# 
		self._listBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._listBox1.FormattingEnabled = True
		self._listBox1.ItemHeight = 29
		self._listBox1.Location = System.Drawing.Point(30, 24)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(895, 265)
		self._listBox1.TabIndex = 0
		self._listBox1.SelectedIndexChanged += self.ListBox1SelectedIndexChanged
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(96, 336)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(149, 60)
		self._button1.TabIndex = 1
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(395, 336)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(152, 61)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(659, 335)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(142, 61)
		self._button3.TabIndex = 3
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ActiveCaption
		self.ClientSize = System.Drawing.Size(947, 429)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._listBox1)
		self.Name = "MainForm"
		self.Text = "ahh"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		header = "Number:" + "\t\t" + "Cube Root:" + "\t\t" + "Num Cubed:"
		self._listBox1.Items.Add(header)
		for num in range(-25,26):
			nc  = num**3
			ncr = num
			if ncr <=0:
				ncr2 = -(abs(ncr)**(1.0/3))
			else: 
				ncr2 = (abs(num)**(1.0/3))
			ncr2r = round(ncr2, 5)
			
			line = str(num) + "\t\t" + str(ncr2r) + "\t\t\t" + str(nc)
			self._listBox1.Items.Add(line)

	def ListBox1SelectedIndexChanged(self, sender, e):
		pass

	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()

	def Button3Click(self, sender, e):
		Application.Exit()