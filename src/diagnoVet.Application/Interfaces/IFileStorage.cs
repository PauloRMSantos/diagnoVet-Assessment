namespace diagnoVet.Application.Interfaces;

public interface IFileStorage
{
    Task<string> UploadPdfAsync(Stream file, string fileName);
    Task<string> UploadImageAsync(byte[] content, string path);
}