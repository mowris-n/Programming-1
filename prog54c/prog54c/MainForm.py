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
        self._textBox1 = System.Windows.Forms.TextBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(76, 110)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(178, 36)
        self._label1.TabIndex = 0
        self._label1.Text = "Radius"
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(76, 170)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(178, 36)
        self._label2.TabIndex = 1
        self._label2.Text = "Area"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(76, 235)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(178, 36)
        self._label3.TabIndex = 2
        self._label3.Text = "Circumference"
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(331, 235)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(178, 36)
        self._label4.TabIndex = 3
        self._label4.Click += self.Label4Click
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(331, 170)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(178, 36)
        self._label5.TabIndex = 4
        self._label5.Click += self.Label5Click
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(331, 107)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(178, 35)
        self._textBox1.TabIndex = 5
        self._textBox1.TextChanged += self.TextBox1TextChanged
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(46, 330)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(208, 54)
        self._button1.TabIndex = 6
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(341, 330)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(208, 54)
        self._button2.TabIndex = 7
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(631, 330)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(208, 54)
        self._button3.TabIndex = 8
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Maroon
        self.ClientSize = System.Drawing.Size(934, 407)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "prog54c"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button3Click(self, sender, e):
        Application.Exit()

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._label5.Text = ""
        self._label4.Text = ""
                

    def Button1Click(self, sender, e):
        Pi = float(3.14159)
        Radius = float(self._textBox1.Text)
        Circumference = 2 * Pi * Radius
        Area = Pi * Radius **2
        self._label4.Text = "%.3f" %(Circumference)
        self._label5.Text = "%.3f" %(Area)
                
        

    def TextBox1TextChanged(self, sender, e):
        pass

    def Label6Click(self, sender, e):
        pass

    def Label5Click(self, sender, e):
        pass

    def Label4Click(self, sender, e):
        pass