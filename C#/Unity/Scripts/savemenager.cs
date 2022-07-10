using System.IO;
using System.Runtime.Serialization.Formatters.Binary;
using UnityEngine;


public class savemenager 
{

    public static void saveplayers (values p)
    {
        BinaryFormatter fm = new BinaryFormatter();
        playersdata data = new playersdata(p);
        string path = Application.persistentDataPath + "/"+"campaign"+".ucg";
        FileStream stream = new FileStream(path, FileMode.Create);
        fm.Serialize(stream, data);
        stream.Close();
    }


    public static playersdata loadplayers()
    {

        string path = Application.persistentDataPath + "/"+"campaign"+".ucg";
        if (File.Exists(path))
        {
            BinaryFormatter fm = new BinaryFormatter();
            FileStream stream = new FileStream(path, FileMode.Open);
            playersdata data = fm.Deserialize(stream) as playersdata;
            stream.Close();
            Debug.Log("Done");
            return data;
        }
        else
        {
            Debug.LogError("Not Found");
            return null;
        }
    }
}
