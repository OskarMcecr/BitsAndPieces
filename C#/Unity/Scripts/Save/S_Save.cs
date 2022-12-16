using UnityEngine;
using System.IO;
using System.Runtime.Serialization.Formatters.Binary;

public static class S_Save
{
    public static void SavePlayer (P_Status PlayerStatus)
    {
        BinaryFormatter formatter = new BinaryFormatter();
        string SavePath = Application.persistentDataPath + "/save.him";
        FileStream stream = new FileStream(SavePath, FileMode.Create);

        S_SaveData data = new S_SaveData(PlayerStatus);

        formatter.Serialize(stream,data);
        stream.Close();
    }
}
