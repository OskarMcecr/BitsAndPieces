using UnityEngine;

public class InterObjectTest : MonoBehaviour
{
    private Camera _mainCamera;
    private Renderer _renderer;
    private Ray _ray;
    private RaycastHit _hit;

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
                    _renderer.material.color =
                        _renderer.material.color == Color.red ? Color.blue : Color.red;
                }
            }
        }
    }
}
