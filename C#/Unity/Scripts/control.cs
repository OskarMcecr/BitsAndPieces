using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class control : MonoBehaviour
{
    public void Play()
    {
        SceneManager.LoadScene("LoadGame");
    }
    public void LoadGame()
    {
        SceneManager.LoadScene("LoadGame");
    }

    public void MainMenu()
    {
        SceneManager.LoadScene("Menu");
    }

    public void exit()
    {
        Debug.Log("Exit");
        Application.Quit();
    }
}
