namespace practica1_edd
{
    partial class administrarMensajescs
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.btnEnviarM = new System.Windows.Forms.Button();
            this.btnCola = new System.Windows.Forms.Button();
            this.btnRespuesta = new System.Windows.Forms.Button();
            this.btnRegresar = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // btnEnviarM
            // 
            this.btnEnviarM.Location = new System.Drawing.Point(390, 166);
            this.btnEnviarM.Name = "btnEnviarM";
            this.btnEnviarM.Size = new System.Drawing.Size(252, 79);
            this.btnEnviarM.TabIndex = 0;
            this.btnEnviarM.Text = "Enviar mensaje";
            this.btnEnviarM.UseVisualStyleBackColor = true;
            this.btnEnviarM.Click += new System.EventHandler(this.btnEnviarM_Click);
            // 
            // btnCola
            // 
            this.btnCola.Location = new System.Drawing.Point(345, 301);
            this.btnCola.Name = "btnCola";
            this.btnCola.Size = new System.Drawing.Size(360, 79);
            this.btnCola.TabIndex = 1;
            this.btnCola.Text = "Ver Cola Mensajes";
            this.btnCola.UseVisualStyleBackColor = true;
            this.btnCola.Click += new System.EventHandler(this.btnCola_Click);
            // 
            // btnRespuesta
            // 
            this.btnRespuesta.Location = new System.Drawing.Point(328, 434);
            this.btnRespuesta.Name = "btnRespuesta";
            this.btnRespuesta.Size = new System.Drawing.Size(400, 79);
            this.btnRespuesta.TabIndex = 2;
            this.btnRespuesta.Text = "Ver Respuesta Mensaje";
            this.btnRespuesta.UseVisualStyleBackColor = true;
            // 
            // btnRegresar
            // 
            this.btnRegresar.Location = new System.Drawing.Point(45, 615);
            this.btnRegresar.Name = "btnRegresar";
            this.btnRegresar.Size = new System.Drawing.Size(153, 64);
            this.btnRegresar.TabIndex = 3;
            this.btnRegresar.Text = "Regresar";
            this.btnRegresar.UseVisualStyleBackColor = true;
            this.btnRegresar.Click += new System.EventHandler(this.btnRegresar_Click);
            // 
            // administrarMensajescs
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(16F, 31F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1060, 731);
            this.Controls.Add(this.btnRegresar);
            this.Controls.Add(this.btnRespuesta);
            this.Controls.Add(this.btnCola);
            this.Controls.Add(this.btnEnviarM);
            this.Name = "administrarMensajescs";
            this.Text = "administrarMensajescs";
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button btnEnviarM;
        private System.Windows.Forms.Button btnCola;
        private System.Windows.Forms.Button btnRespuesta;
        private System.Windows.Forms.Button btnRegresar;
    }
}