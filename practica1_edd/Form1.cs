using System;
using System.Collections.Generic;
using System.Collections.Specialized;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace practica1_edd
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            
        }
        public string getCarnet()
        {
            using (WebClient cliente = new WebClient())
            {
                String valor = cliente.DownloadString("http://127.0.0.1:5000/");
                return valor;
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            OpenFileDialog openFileDialog1 = new OpenFileDialog();
            openFileDialog1.Filter = "JSON Files|*.json";
            openFileDialog1.Title = "Select a Cursor File";
            String url = "";

            if (openFileDialog1.ShowDialog() == System.Windows.Forms.DialogResult.OK)
            {
                System.IO.StreamReader sr = new
                   System.IO.StreamReader(openFileDialog1.FileName);
                //MessageBox.Show(openFileDialog1.FileName);
                sr.Close();
                using (WebClient cliente = new WebClient())
                {
                    url = openFileDialog1.FileName;
                    cliente.Encoding = System.Text.Encoding.UTF8;
                    var values = new NameValueCollection();
                    values["url"] = url;
                    var response= cliente.UploadValues("http://127.0.0.1:5000/ServicePrueba", values);
                    var responseString = Encoding.Default.GetString(response);
                    MessageBox.Show(responseString);
                }
                
                btnDashboard.Enabled = true;
                btnAdministrar.Enabled = true;
                btnReporte.Enabled = true;
            }

        }

        private void btnDashboard_Click(object sender, EventArgs e)
        {
            dashboard frm2 = new dashboard();

            frm2.Show();
           
        }

        private void btnAdministrar_Click(object sender, EventArgs e)
        {
            administrarMensajescs adminMens = new administrarMensajescs();
            adminMens.Show();
        }

        private void btnReporte_Click(object sender, EventArgs e)
        {
            mostrarReporte mostrar = new mostrarReporte();
            mostrar.Show();
        }
    }
}
