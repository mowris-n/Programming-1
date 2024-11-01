import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._listBox1 = System.Windows.Forms.ListBox()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 333)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(229, 64)
        self._button1.TabIndex = 4
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(301, 333)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(229, 64)
        self._button2.TabIndex = 5
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(594, 333)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(229, 64)
        self._button3.TabIndex = 6
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # listBox1
        # 
        self._listBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._listBox1.FormattingEnabled = True
        self._listBox1.ItemHeight = 25
        self._listBox1.Location = System.Drawing.Point(12, 12)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(811, 279)
        self._listBox1.TabIndex = 7
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Thistle
        self.ClientSize = System.Drawing.Size(863, 419)
        self.Controls.Add(self._listBox1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "prog152a"
        self.ResumeLayout(False)


    def Label1Click(self, sender, e):
        pass

    def TextBox1TextChanged(self, sender, e):
        pass

    def Button1Click(self, sender, e): 
        heading = "Multiple\t\tSum"
        self._listBox1.Items.Add(heading)
        
        s = 0
        for v in range(0, 9669+1,3):
            s += v
            vs = str(v) + "\t\t" + str(s)
            self._listBox1.Items.Add(vs)
            


    def Button2Click(self, sender, e):
        self._listBox1.Items.Clear()

    def Button3Click(self, sender, e):
        Application.Exit()