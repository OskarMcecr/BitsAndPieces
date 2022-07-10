using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class values : MonoBehaviour
{
    public string campaign,player;
    public int playerN1, playerN2;
    public int playerHP, playerEN, playerWIT;
    public GameObject inputFieldP1,textDisplayP1,textDisplayP1Deck;


    public void ReadCampaignInput(string Campaign)
    {
        campaign = Campaign;
        Debug.Log(campaign);
    }


    public void ReadPInput(string Player)
    {
        player = Player;
        textDisplayP1.GetComponent<Text>().text=player;
        textDisplayP1Deck.GetComponent<Text>().text=player;
        Debug.Log(player);
    }

    public void ReadHPInput(string HP)
    {
        int.TryParse(HP, out playerHP);
        Debug.Log(playerHP);
    }

    public void ReadENInput(string EN)
    {
        int.TryParse(EN, out playerEN);
        Debug.Log(playerEN);
    }

    public void ReadWITInput(string WIT)
    {
        int.TryParse(WIT, out playerWIT);
        Debug.Log(playerWIT);
    }

    public void saveplayers ()
    {
        savemenager.saveplayers(this);
        Debug.Log(Application.persistentDataPath);
    }

    public void loadplayers ()
    {
        playersdata p = savemenager.loadplayers();

        campaign = p.campaign;
        player = p.player;
        playerHP = p.playerHP;
        playerEN = p.playerEN;
        playerWIT = p.playerWIT;
        Debug.Log("Done");
    }

    [HideInInspector] public ABRarity ABrarity;
    public enum ABRarity
        {
            Nature,
            Entry
        }

    [HideInInspector] public ABType ABtype;
    public enum ABType
        {
            Attack,
            Block,
            Passive
        }

    [HideInInspector] public ENRarity ENrarity;
    public enum ENRarity
        {
            Roach,
            Alfa,
            Ancient
        }

    [HideInInspector] public KeywordDescription keywordDescription;
    public enum KeywordDescription
        {
            Curse,
            Cripple,
            Expose,
            FollowUp
        }

}


