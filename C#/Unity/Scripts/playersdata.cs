using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[System.Serializable]
public class playersdata 
{
    public string campaign,player;
    public int playerN1, playerN2;
    public int playerHP, playerEN, playerWIT;

    public playersdata (values p)
    {
        campaign = p.campaign;
        player = p.player;
        playerHP = p.playerHP;
        playerEN = p.playerEN;
        playerWIT = p.playerWIT;
        Debug.Log("Done");
    }
}
