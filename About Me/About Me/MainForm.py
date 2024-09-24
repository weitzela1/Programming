import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._textBox1 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.DarkOliveGreen
		self._textBox1.Font = System.Drawing.Font("Rockwell", 36, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.ForeColor = System.Drawing.SystemColors.ControlLightLight
		self._textBox1.Location = System.Drawing.Point(116, 60)
		self._textBox1.Multiline = True
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(732, 275)
		self._textBox1.TabIndex = 0
		self._textBox1.Text = "My name is Anthony Weitzel and I am fourteen years old. I like to play and watch sports and hope to become an orthodontist as a adult."
		self._textBox1.TextChanged += self.TextBox1TextChanged
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.DarkGreen
		self.ClientSize = System.Drawing.Size(900, 622)
		self.Controls.Add(self._textBox1)
		self.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
		self.Name = "MainForm"
		self.Text = "About Me"
		self.ResumeLayout(False)
		self.PerformLayout()


	def TextBox1TextChanged(self, sender, e):
		pass