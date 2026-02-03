using diagnoVet.Domain.Entities;

namespace diagnoVet.Application.Interfaces;

public interface IReportRepository
{
    Task SaveAsync(Report report);
    Task<Report?> GetByIdAsync(Guid id);
}