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
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._textBox4 = System.Windows.Forms.TextBox()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Thistle
        self._label1.Location = System.Drawing.Point(56, 25)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(180, 36)
        self._label1.TabIndex = 0
        self._label1.Text = "variable1"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.Thistle
        self._label2.Location = System.Drawing.Point(56, 82)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(180, 36)
        self._label2.TabIndex = 1
        self._label2.Text = "variable2"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(263, 29)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(147, 29)
        self._textBox1.TabIndex = 2
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(262, 86)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(147, 29)
        self._textBox2.TabIndex = 3
        # 
        # textBox3
        # 
        self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.Location = System.Drawing.Point(706, 87)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(147, 29)
        self._textBox3.TabIndex = 7
        # 
        # textBox4
        # 
        self._textBox4.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox4.Location = System.Drawing.Point(707, 30)
        self._textBox4.Name = "textBox4"
        self._textBox4.Size = System.Drawing.Size(147, 29)
        self._textBox4.TabIndex = 6
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.Thistle
        self._label3.Location = System.Drawing.Point(500, 83)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(180, 36)
        self._label3.TabIndex = 5
        self._label3.Text = "variable4"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.Thistle
        self._label4.Location = System.Drawing.Point(500, 26)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(180, 36)
        self._label4.TabIndex = 4
        self._label4.Text = "variable3"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.White
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
        self._label5.Location = System.Drawing.Point(155, 154)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(190, 55)
        self._label5.TabIndex = 8
        self._label5.Text = "Sum"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.White
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
        self._label6.Location = System.Drawing.Point(554, 154)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(190, 55)
        self._label6.TabIndex = 9
        self._label6.Text = "Avg"
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.Plum
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
        self._label7.Location = System.Drawing.Point(155, 225)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(190, 55)
        self._label7.TabIndex = 10
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.Plum
        self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
        self._label8.Location = System.Drawing.Point(554, 225)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(190, 55)
        self._label8.TabIndex = 11
        self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(51, 313)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(185, 56)
        self._button1.TabIndex = 12
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(356, 313)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(185, 56)
        self._button2.TabIndex = 13
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(668, 313)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(185, 56)
        self._button3.TabIndex = 14
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.MediumOrchid
        self.ClientSize = System.Drawing.Size(934, 394)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "prog54b"
        self.Load += self.MainFormLoad
        self.ResumeLayout(False)
        self.PerformLayout()


    def MainFormLoad(self, sender, e):
        pass

    def Button1Click(self, sender, e):
        variable1 = int(self._textBox1.Text)
        variable2 = int(self._textBox2.Text)
        variable3 = int(self._textBox3.Text)
        variable4 = int(self._textBox4.Text)
        total = variable1 + variable2 + variable3 + variable4 
        Avg = total / 4.0
        self._label7.Text = str(total)
        self._label8.Text = str(Avg)

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._textBox3.Text = ""
        self._textBox4.Text = ""
        self._label7.Text = ""
        self._label8.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()