using UnityEngine;
public class InterObjectTest : MonoBehaviour
{
    private Camera _mainCamera;
    private Renderer _renderer;
    private Ray _ray;
    private RaycastHit _hit;
    public InterPause pState;

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
                    Debug.Log("Click");
                    pState.PauseState = 2;
                    SwitchBoards();
                }
            }
        }
    }

    private void SwitchBoards()
    {
        _mainCamera.transform.position = new Vector3(-8.5f,12f,8.5f+200.0f);
        _mainCamera.transform.Rotate(new Vector3(90, 0, 0));
    }
}
