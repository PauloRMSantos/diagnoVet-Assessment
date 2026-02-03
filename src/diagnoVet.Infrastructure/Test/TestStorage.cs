using diagnoVet.Application.Interfaces;

namespace diagnoVet.Infrastructure.Test;

public class TestStorage : IFileStorage
{
    public Task<string> UploadPdfAsync(Stream pdf, string fileName)
    {
        return Task.FromResult($"gs://test-bucket/{fileName}");
    }

    public Task<string> UploadImageAsync(byte[] content, string path)
    {
        return Task.FromResult($"https://test/{path}");
    }
}