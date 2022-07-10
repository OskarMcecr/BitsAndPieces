using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Abilities : MonoBehaviour
{
    public CardCreatorAbility card;
    void Start()
    {
        Debug.Log(card.name);
        Debug.Log(card.MainDescription);
    }
}
