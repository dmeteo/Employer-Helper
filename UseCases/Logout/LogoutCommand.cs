using MediatR;

namespace EmployeeHelper.UseCases.Logout;

public record LogoutCommand : IRequest<Unit>;
