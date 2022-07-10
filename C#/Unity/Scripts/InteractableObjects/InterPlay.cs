using UnityEngine;

public class InterPlay : MonoBehaviour
{
    private Camera _mainCamera;
    private Renderer _renderer;
    private Ray _ray;
    private RaycastHit _hit;
    public int Pause = 1;

    private void Start()
    {
        _mainCamera = Camera.main;
        _renderer = GetComponent<Renderer>();
    }

    private void Update()
    {
        if (Input.GetMouseButtonDown(0))
        {
            _ray = new Ray(_mainCamera.ScreenToWorldPoint(Input.mousePosition), _mainCamera.transform.forward);
            if (Physics.Raycast(_ray, out _hit, 200.0f))
            {
                if (_hit.transform == transform)
                {
                    Debug.Log("Play");
                    Pause = 0;
                    Camera.main.transform.Rotate(new Vector3(90, 0, 0));
                }
            }
        }
        if (Input.GetKeyDown(KeyCode.Escape) && Pause == 0)
        {
            Debug.Log("Pause");
            Pause = 1;
            Camera.main.transform.Rotate(new Vector3(-90, 0, 0));
        }
    }
}
