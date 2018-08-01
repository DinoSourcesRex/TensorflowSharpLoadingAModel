using System;
using System.IO;
using TensorFlow;

namespace LoadingAModel
{
    public class Program
    {
        public static void Main(string[] args)
        {
            var graph = new TFGraph();

            var model = File.ReadAllBytes("savepath/saved_model.pb");

            graph.Import(model);

            Console.ReadKey();
        }
    }
}
