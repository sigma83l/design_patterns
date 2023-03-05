using System;
    Singleton s1 = Singleton.Instance();
    Singleton s2 = Singleton.Instance();
    if (s1 == s2)
    {
        Console.WriteLine("success");
    }
    Console.ReadKey();
    public class Singleton
    {
        static Singleton instance;
        protected Singleton()
        {
        }
        public static Singleton Instance()
        {
            if (instance == null)
            {
                instance = new Singleton();
            }
            return instance;
        }
    }

