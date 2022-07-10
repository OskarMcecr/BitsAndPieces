using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[CreateAssetMenu(fileName = "New Enemy", menuName = "Heresy/Board/Enemy")]
public class CardCreatorEnemy : ScriptableObject
{
    [Header("Basic")]
    public new string name;
    public int ID;
    public Sprite EnemyImage;
    public values.ENRarity Rarity;

    [Header("Passive")]
    public string MainDescription;
    public string KeywordDescription;

    [Header("First move")]
    public int FirstMinRange;
    public int FirstMaxRange;
    public string FirstDescription;

    [Header("Second move")]
    public int SecondMinRange;
    public int SecondMaxRange;
    public string SecondDescription;

    [Header("Third move")]
    public int ThirdMinRange;
    public int ThirdMaxRange;
    public string ThirdDescription;
}   
