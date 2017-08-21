using System;
using System.Collections.Generic;
using System.Collections.Specialized;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Net;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace practica1_edd
{
    public partial class envioMensaje : Form
    {
        OpenFileDialog openFileDialog1 = new OpenFileDialog();
        Boolean bandera = false;
        public envioMensaje()
        {
            InitializeComponent();
        }

        private void btnCargarXML_Click(object sender, EventArgs e)
        {

           
            openFileDialog1.Filter = "XML Files|*.xml";
            openFileDialog1.Title = "Selecciona archivo xml";

            if (openFileDialog1.ShowDialog() == System.Windows.Forms.DialogResult.OK)
            {
                richTextBox1.LoadFile(openFileDialog1.FileName, RichTextBoxStreamType.PlainText);
                
            }
            bandera = true;
        }

        private void btnAceptar_Click(object sender, EventArgs e)
        {
            if (bandera) {
                using (WebClient cliente = new WebClient())
                {
                    
                    cliente.Encoding = System.Text.Encoding.UTF8;
                    var values = new NameValueCollection();
                    String prueba = richTextBox1.Text;
                    values["cadena"] = openFileDialog1.FileName;
                    var response = cliente.UploadValues("http://127.0.0.1:5000/serviceagregarmensaje", values);
                    var responseString = Encoding.Default.GetString(response);
                    MessageBox.Show(responseString);
                }
            }
            else
            {

            }
        }

        private void btnCancelar_Click(object sender, EventArgs e)
        {
            administrarMensajescs frm2 = new administrarMensajescs();
            frm2.Show();
            this.Close();
        }
        public string getCarnet() {
            using (WebClient cliente = new WebClient()) {
                String valor =  cliente.DownloadString("http://127.0.0.1:5000/");
                return valor;
            }
            
            

        }
    }
}
