using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CharacterControler : MonoBehaviour
{
    public GameObject[] CharacterModel;
    public float moveSpeed = 5f;
    public Transform movePoint;
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.W))
        {
            Debug.Log("Pause");
        }
    }
}
