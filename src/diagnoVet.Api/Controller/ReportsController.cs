using diagnoVet.Application.UseCases;
using Microsoft.AspNetCore.Mvc;

[ApiController]
[Route("api/[controller]")]
public class ReportsController : ControllerBase
{
    private readonly UploadReportUseCase _uploadReportUseCase;

    public ReportsController(UploadReportUseCase uploadReportUseCase)
    {
        _uploadReportUseCase = uploadReportUseCase;
    }

    [HttpPost]
    public async Task<IActionResult> UploadReport(IFormFile file)
    {
        if (file == null || file.Length == 0)
        {
            return BadRequest("No file uploaded.");
        }

        var id = await _uploadReportUseCase.ExecuteAsync(file.OpenReadStream());

        return Accepted(new { reportId = id });
    }
}