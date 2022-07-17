using UnityEngine;

public class gridprefab : MonoBehaviour
{
    public GameObject[] baseBlocks;
    public GameObject[] treePrefabs;
    public GameObject[] terrainPrefabs;
    public float baseLevel = .4f;
    public float highLevel = .8f;
    public float treeNoiseScale = .05f;
    public float treeDensity = .5f;
    public float terrainNoiseScale = .05f;
    public float terrainDensity = .2f;
    public float height = 1.2f;
    public float scale = .1f;
    public int size = 0;
    int startingLevel = 0;

    Cell[,] grid;

    void Start() {
        float[,] noiseMap = new float[size, size];
        float[,] noiseMapTree = new float[size, size];
        float[,] noiseMapTerrain = new float[size, size];
        (float xOffset, float zOffset) = (Random.Range(-10000f, 10000f), Random.Range(-10000f, 10000f));
        (float xtrOffset, float ztrOffset) = (Random.Range(-10000f, 10000f), Random.Range(-10000f, 10000f));
        (float xteOffset, float zteOffset) = (Random.Range(-10000f, 10000f), Random.Range(-10000f, 10000f));
        for(int z = 3; z < size; z++) 
        {
            for(int x = 3; x < size; x++)
            {
                float noiseValue = Mathf.PerlinNoise(x * scale + xOffset, z * scale + zOffset);
                noiseMap[x, z] = noiseValue;
                float noiseValueTree = Mathf.PerlinNoise(x * treeNoiseScale + xtrOffset, z * treeNoiseScale + ztrOffset);
                noiseMapTree[x, z] = noiseValueTree;
                float noiseValueTerrain = Mathf.PerlinNoise(x * terrainNoiseScale + xteOffset, z * terrainNoiseScale + zteOffset);
                noiseMapTerrain[x, z] = noiseValueTerrain;
            }
        }

        float[,] falloffMap = new float[size,size];
        for(int z = 0; z < size; z++){
            for(int x = 0; x < size; x++){
                float xv = x/(float)size *2 -1;
                float zv = z/(float)size *2 -1;
                float v = Mathf.Max(Mathf.Abs(xv), Mathf.Abs(zv));
                falloffMap[x, z] = Mathf.Pow(v, 3f) / (Mathf.Pow(v, 3f) + Mathf.Pow(2.2f - 2.2f * v, 3f));
        }
        }

        grid = new Cell[size, size];
        for(int z = 0; z < size; z++)
         {
            for(int x = 0; x < size; x++) 
            {
                float bHeight = height;
                float noiseValue = noiseMap[x, z];
                noiseValue -= falloffMap[x, z];
                float noiseValueTree = noiseMapTree[x, z];
                float noiseValueTerrain = noiseMapTerrain[x, z];
                bool isBaseLevel = noiseValue < baseLevel;
                Cell cell = new Cell(isBaseLevel);
                grid[x, z] = cell;
                Vector3 pos = new Vector3(.5f+(x-size/2), 0, .5f+z-(size/2));
                if(cell.isBaseLevel)
                    {
                    startingLevel = 0;
                    bHeight = -height;
                    }
                else if(noiseValue > highLevel)
                    {
                    startingLevel = baseBlocks.Length-1;
                    bHeight = height;
                    }
                else
                    {
                    startingLevel = 1;
                    bHeight = 0;
                    }

                GameObject block = Instantiate(baseBlocks[startingLevel],pos,Quaternion.identity);
                
                if(!cell.isBaseLevel)
                {
                    float vtr = Random.Range(0f, treeDensity);
                    if(noiseValueTree < vtr)
                    {
                        GameObject prefab = treePrefabs[Random.Range(0, treePrefabs.Length)];
                        GameObject tree = Instantiate(prefab, transform);
                        tree.transform.position = new Vector3(.5f+(x-size/2), bHeight, .5f+(z-size/2));
                        tree.transform.rotation = Quaternion.Euler(0, Random.Range(0, 360f), 0);
                        tree.transform.localScale = Vector3.one * Random.Range(.8f, 1.2f);
                    }
                    float vte = Random.Range(0f, terrainDensity);
                    if(noiseValueTerrain < vte)
                    {
                        GameObject prefab = terrainPrefabs[Random.Range(0, terrainPrefabs.Length)];
                        GameObject terrain = Instantiate(prefab, transform);
                        terrain.transform.position = new Vector3(.5f+(x-size/2), bHeight, .5f+(z-size/2));
                        terrain.transform.rotation = Quaternion.Euler(0, Random.Range(0, 360f), 0);
                    }
                }
            }
        }
    }
}