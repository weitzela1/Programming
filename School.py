
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Form1(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Rockwell", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(177, 75)
		self._textBox1.Multiline = True
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(522, 113)
		self._textBox1.TabIndex = 0
		self._textBox1.Text = "\"To the world you may be one person but to one person you may be the world\""
		self._textBox1.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
		self._textBox1.TextChanged += self.TextBox1TextChanged
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Rockwell", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(210, 204)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(468, 101)
		self._label1.TabIndex = 1
		self._label1.Text = "Dr. Suess"
		self._label1.TextAlign = System.Drawing.ContentAlignment.TopCenter
		self._label1.Click += self.Label1Click
		# 
		# Form1
		# 
		self.ClientSize = System.Drawing.Size(898, 645)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox1)
		self.Name = "Form1"
		self.Text = "Form1"
		self.Load += self.Form1Load
		self.ResumeLayout(False)
		self.PerformLayout()


	def Form1Load(self, sender, e):
		pass

	def TextBox1TextChanged(self, sender, e):
		pass

	def Label1Click(self, sender, e):
		pass