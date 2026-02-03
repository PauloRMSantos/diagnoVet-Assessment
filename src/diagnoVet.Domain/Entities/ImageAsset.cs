namespace diagnoVet.Domain.Entities;

public class ImageAsset
{
    public string Url { get; }

    public ImageAsset(string url)
    {
        Url = url;
    }
}