using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[CreateAssetMenu(fileName = "New Trait", menuName = "Heresy/Cards/Trait")]
public class CardCreatorTrait : ScriptableObject
{
    [Header("Basic")]
    public new string name;
    public int ID;
    public Sprite CardImage;

    [Header("Description")]
    public string MainDescription;
    public string KeywordDescription;
}   
