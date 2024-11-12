using EmployeeHelper.Domain;
using MediatR;
using Microsoft.AspNetCore.Identity;

namespace EmployeeHelper.UseCases.Logout;

public class LogoutCommandHandler : IRequestHandler<LogoutCommand, Unit>
{
    private SignInManager<User> signInManager;

    public LogoutCommandHandler(SignInManager<User> signInManager)
    {
        this.signInManager = signInManager;
    }

    public async Task<Unit> Handle(LogoutCommand request, CancellationToken cancellationToken)
    {
        await signInManager.SignOutAsync();

        return Unit.Value;
    }
}
