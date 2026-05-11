# Stored Procedure: `GetDongBoThucChayToHDCNByPrameters`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-16 10:07:46.023000
- **Ngày sửa cuối**: 2014-11-19 12:17:54.917000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@pPhanBoID` | `nvarchar(100)` | No |
| `@pSoLuongThucChay` | `nvarchar(100)` | No |
| `@pThanhTienThucChay` | `nvarchar(100)` | No |
| `@pThucChayDenNgay` | `datetime(8)` | No |
| `@pThoiGianBatDau` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--GetDongBoThucChayToHDCNByPrameters @pPhanBoID='66368',@pSoLuongThucChay='33220001',@pThanhTienThucChay='1664000001.048',@pThucChayDenNgay='10/5/2014 12:00:00 AM',@pThoiGianBatDau='10/5/2014 12:00:00 AM'

CREATE PROCEDURE [dbo].[GetDongBoThucChayToHDCNByPrameters] 
	-- Add the parameters for the stored procedure here
	@pPhanBoID NVARCHAR(50)
	,@pSoLuongThucChay NVARCHAR(50)
	,@pThanhTienThucChay NVARCHAR(50)
	,@pThucChayDenNgay DATETIME
	,@pThoiGianBatDau DATETIME
AS
BEGIN

DECLARE @NgayThucHienMin DATETIME, @NgayThucHienMax DATETIME

SET @NgayThucHienMin = (SELECT 	Min(NgayThucHien) FROM dbo.SysThuChay_HDCNLog
						 Where	
						 MaHanhDong = 1	
						 AND IsHanhDong = 1	
						 AND IsDongBo = 0
						 )	

SET @NgayThucHienMin = ISNULL(@NgayThucHienMin,GETDATE())				 
						 
SET @NgayThucHienMax = (SELECT 	Max(NgayThucHien) FROM dbo.SysThuChay_HDCNLog
						 Where	
						 MaHanhDong = 1	
						 AND IsHanhDong = 1	
						 AND IsDongBo = 0
						 )	

SET @NgayThucHienMax = ISNULL(@NgayThucHienMax,GETDATE())	
	
select        
 T.id      
 ,T.SoLuongThucChay      
 ,T.ThanhTienThucChay      
 ,Convert(date,(select max(I.NgayThucHien) from ThucChayDaTinh I where I.HopDongChiTietREF = T.id)) AS ThucChayDenNgay      
 ,Convert(date,(select min(I.NgayThucHien) from ThucChayDaTinh I where I.HopDongChiTietREF = T.id)) AS ThoiGianBatDau      
 from      
 (      
  SELECT      
      A.HopDongChiTietREF AS id,    
      SUM(A.SoLuongThucChay) AS SoLuongThucChay,    
      (SUM(A.ThanhTienSauTrietKhauThucChay) + SUM(A.GiaTriThayDoi)) AS ThanhTienThucChay    
  FROM   ThucChayDaTinh A     
      INNER JOIN HopDongChiTiet B    
     ON  A.HopDongChiTietREF = B.HopDongChiTietID  
  WHERE  1 = 1     
      AND A.SoHopDong <> ''    
      AND A.SoHopDong IS NOT NULL    
      AND A.SoHopDong <> '-'    
      AND A.TrangThaiHopDong <> 3    
      AND A.HopDongChiTietREF <> 0    
      AND A.HopDongChiTietREF <> 0             
      AND A.HopDongChiTietREF IN (SELECT HopDongChiTietREF  FROM ThucChayDaTinh WHERE  NgayThucHien BETWEEN  @NgayThucHienMin AND @NgayThucHienMax)    
  GROUP BY     
      A.HopDongChiTietREF    
 )T      
    
order by T.id

END

```
