using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[CreateAssetMenu(fileName = "New Ability", menuName = "Heresy/Cards/Ability")]
public class CardCreatorAbility : ScriptableObject
{
    [Header("Basic")]
    public new string name;
    public int ID;
    public values.ABRarity Rarity;
    public values.ABType Type;
    public Sprite CardImage;

    [Header("Description")]
    public string MainDescription;

    [Header("Cost")]
    public int ENCost;
    public int RESCost;

    [Header("Damage/Block")]
    public int DMG;
    public int BLK;

    [Header("Card advantage")]
    public int CardsDrawn;
    public int CardsDiscarded;
    
    [Header("Keywords")]
    public string[] KeywordName;
    public int[] KeywordValue;

    [Header("Gain")]
    public int ENGain;
    public int RESGain;
}   
