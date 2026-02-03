namespace diagnoVet.Domain.Entities;

public class Report
{
    public Guid Id { get; private set; }
    public string Patient { get; private set; }
    public string Owner { get; private set; }
    public string Veterinarian { get; private set; }
    public string Diagnosis { get; private set; }
    public string Recommendations { get; private set; }
    public IReadOnlyList<string> Images => _images;

    private readonly List<string> _images = new();

    private Report() { }

    public Report(
        Guid id,
        string patient,
        string owner,
        string veterinarian,
        string diagnosis,
        string recommendations
    )
    {
        Id = id;
        Patient = patient;
        Owner = owner;
        Veterinarian = veterinarian;
        Diagnosis = diagnosis;
        Recommendations = recommendations;
    }

    public void AddImage(ImageAsset image)
    {
        _images.Add(image.ToString());
    }
    
}