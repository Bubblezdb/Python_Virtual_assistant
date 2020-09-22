using Microsoft.CognitiveServices.Speech;
using System.Threading.Tasks;
using System;
using System.Net;

namespace VirtualAssistant
{
    class Program
    {
        static async Task Main(string[] args)
        {
            var speechConfig = SpeechConfig.FromSubscription("bf72deae03534238bb6d8b885f027f3f", "eastus");
            using var recognizer = new SpeechRecognizer(speechConfig);
            using var synthesizer = new SpeechSynthesizer(speechConfig);
            string command="Hello, I am Roscoe. Your Personal Assistant";
            await synthesizer.SpeakTextAsync(command);
            var result = await recognizer.RecognizeOnceAsync();
             command = result.Text.ToLower();
                
            
            //create a loop function
            //create commands
            //keep service running in the background


            switch (result.Reason)
            {
                case ResultReason.RecognizedSpeech:
                    Console.WriteLine($"RECOGNIZED: You said {command}");
                    await synthesizer.SpeakTextAsync(command);
                    Functionality(command);
                    break;
                case ResultReason.NoMatch:
                    Console.WriteLine($"NOMATCH: Speech could not be recognized.");
                    break;
                case ResultReason.Canceled:
                    var cancellation = CancellationDetails.FromResult(result);
                    Console.WriteLine($"CANCELED: Reason={cancellation.Reason}");

                    if (cancellation.Reason == CancellationReason.Error)
                    {
                        Console.WriteLine($"CANCELED: ErrorCode={cancellation.ErrorCode}");
                        Console.WriteLine($"CANCELED: ErrorDetails={cancellation.ErrorDetails}");
                        Console.WriteLine($"CANCELED: Did you update the subscription info?");
                    }
                    break;
            }
        }
        
        static void Functionality(string command)
        {
            if (command == "Hey Roscoe!" || command == "Roscoe!")
                if (command == "spotify")
                {
                    var request = (HttpWebRequest)WebRequest.Create("www.spotify.com");
                    request.GetResponse();
                }

        }
    }
}
