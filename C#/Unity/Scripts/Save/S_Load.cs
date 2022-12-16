using UnityEngine;
using System.IO;
using System.Runtime.Serialization.Formatters.Binary;

public static class S_Load
{
    public static S_SaveData LoadPlayer()
    {
        string SavePath = Application.persistentDataPath + "/save.him";
        if (File.Exists(SavePath))
        {
            BinaryFormatter formatter = new BinaryFormatter();
            FileStream stream = new FileStream(SavePath, FileMode.Open);
            S_SaveData data = formatter.Deserialize(stream) as S_SaveData;
            stream.Close();
            return data;
        }
        else
        {
            Debug.Log("Save not found");
            return null;
        }
    }
}
