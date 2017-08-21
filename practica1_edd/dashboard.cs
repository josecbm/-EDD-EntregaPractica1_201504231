using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Net;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;
using System.Data;
using Newtonsoft.Json;
using System.Net;
using System.Net.NetworkInformation;

namespace practica1_edd
{
    public partial class dashboard : Form
    {
        public dashboard()
        {
            InitializeComponent();
            string fileJSON = File.ReadAllText(@"C:\Users\jose_\Documents\universidad\segundoSemestre2017\estructuras\practica1\datosfinales.json");
            DataTable dt = (DataTable)JsonConvert.DeserializeObject(fileJSON, typeof(DataTable));
            dataGridView1.DataSource = dt;
            IPHostEntry host;

            lblLocal.Text = "Este Nodo: "+getIp();
        }
        private string getIp() {

            IPHostEntry host;
            string localIP = "";
            host = Dns.GetHostEntry(Dns.GetHostName());
            foreach (IPAddress ip in host.AddressList)
            {
                if (ip.AddressFamily.ToString() == "InterNetwork")
                {
                    localIP = ip.ToString();
                }
            }
            return localIP;
        }

        private void button1_Click(object sender, EventArgs e)
        {

            OpenFileDialog openFileDialog1 = new OpenFileDialog();
            openFileDialog1.Filter = "JSON Files|*.json";
            openFileDialog1.Title = "Seleccione JSON File";

            if (openFileDialog1.ShowDialog() == System.Windows.Forms.DialogResult.OK)
            {
                System.IO.StreamReader sr = new
                   System.IO.StreamReader(openFileDialog1.FileName);
                MessageBox.Show(openFileDialog1.FileName);
                sr.Close();
                
            }
        }
    }
}
