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
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label5 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Gold
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 25)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(168, 56)
        self._label1.TabIndex = 0
        self._label1.Text = "Pounds"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.Gold
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(12, 105)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(168, 56)
        self._label2.TabIndex = 1
        self._label2.Text = "Shillings"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.Gold
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(12, 187)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(168, 56)
        self._label3.TabIndex = 2
        self._label3.Text = "Pence"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.Color.FloralWhite
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(198, 38)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(176, 31)
        self._textBox1.TabIndex = 3
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.Gold
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(408, 25)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(168, 56)
        self._label5.TabIndex = 7
        self._label5.Text = "Decimal Pounds"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.FloralWhite
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(595, 25)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(168, 56)
        self._label7.TabIndex = 9
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox2
        # 
        self._textBox2.BackColor = System.Drawing.Color.FloralWhite
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(198, 118)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(176, 31)
        self._textBox2.TabIndex = 10
        # 
        # textBox3
        # 
        self._textBox3.BackColor = System.Drawing.Color.FloralWhite
        self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.Location = System.Drawing.Point(198, 200)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(176, 31)
        self._textBox3.TabIndex = 11
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FloralWhite
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(50, 322)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(187, 77)
        self._button1.TabIndex = 12
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FloralWhite
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(296, 322)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(187, 77)
        self._button2.TabIndex = 13
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FloralWhite
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(541, 322)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(187, 77)
        self._button3.TabIndex = 14
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Maroon
        self.ClientSize = System.Drawing.Size(791, 422)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "prog65h"
        self.Load += self.MainFormLoad
        self.ResumeLayout(False)
        self.PerformLayout()


    def MainFormLoad(self, sender, e):
        pass

    def Button1Click(self, sender, e):
        Pounds = int(self._textBox1.Text)
        Shillings = int(self._textBox2.Text)
        Pence = int(self._textBox3.Text)
        #20 shillings to a pound, 12 pence to a shilling
        #£5.2.8 meant 5 pounds, 2 shillings and 8 pence.
        #new system is 100 pence to a pound
        s = Shillings *0.05
        pe = Pence * 0.05 * 0.08333
        po = Pounds + s + pe
        self._label7.Text = str(po)        
        
        
        