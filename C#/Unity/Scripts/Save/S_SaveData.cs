using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[System.Serializable]
public class S_SaveData
{
    public int BaseHealth;
    public int BaseWIT;
    public int BaseEN;
    public int CuHealth;
    public int CuWIT;
    public int CuEN;
    public int[] DeckAbil;

    public S_SaveData(P_Status PlayerStatus)
    {
        BaseHealth = PlayerStatus.BaseHealth;
        BaseWIT = PlayerStatus.BaseWIT;
        BaseEN = PlayerStatus.BaseEN;
        CuHealth = PlayerStatus.CuHealth;
        CuWIT = PlayerStatus.CuWIT;
        CuEN = PlayerStatus.CuEN;

        DeckAbil = new int[PlayerStatus.DeckAbil.Count];
        for(int i = 0; i < PlayerStatus.DeckAbil.Count; i++)
        {
            DeckAbil[i] = PlayerStatus.DeckAbil[i];
        }
        Debug.Log("saved deck: "+DeckAbil);
    }
}
