# Stored Procedure: `Gen_InsertOrUpdate_HopDongChiTiet_MuaNgoai_CapNhapTheoDuToan`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2022-05-06 10:33:30.513000
- **Ngày sửa cuối**: 2023-12-21 16:37:39.160000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@FromDate` | `datetime(8)` | No |
| `@ToDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2015-01-13
-- Description:	<Description,,>
-- =============================================
/*
	EXEC  [dbo].[Gen_InsertOrUpdate_HopDongChiTiet_MuaNgoai_CapNhapTheoDuToan] '2022-12-28', '2022-12-30'
*/
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_HopDongChiTiet_MuaNgoai_CapNhapTheoDuToan]
	-- Add the parameters for the stored procedure here
	@FromDate DATETIME,
	@ToDate DATETIME
AS
BEGIN

	SET NOCOUNT ON;

    DECLARE @ngayGioiHanTinh DATETIME  = '2013-01-01'
	, @HopDongChiTietID	INT = 0
			    
	DECLARE MNDuToan_cursor CURSOR FOR

	--SELECT DISTINCT hdct.HopDongChiTietID
	--FROM dbo.ThucChayMuaNgoaiChiTiet mn
	--INNER JOIN dbo.HopDongChiTiet_MuaNgoai hdct ON mn.HopDongChiTietREF = hdct.HopDongChiTietID
	--WHERE hdct.ThanhTienSauCKMua = 0 --dutoan sauck = 0
	--AND CONVERT(DATE,mn.LastModifiedAt) BETWEEN @FromDate AND  @ToDate
	--AND mn.DeletedStatus = 0

	SELECT DISTINCT hdct.HopDongChiTietID
	FROM dbo.ThucChayMuaNgoaiChiTiet mn
	INNER JOIN dbo.HopDongChiTiet_MuaNgoai hdct ON mn.HopDongChiTietREF = hdct.HopDongChiTietID
	WHERE hdct.ThanhTienSauCKMua = 0 --dutoan sauck = 0
	AND ((CONVERT(DATE,mn.LastModifiedAt) BETWEEN @FromDate AND  @ToDate)
	OR ((CONVERT(DATE,mn.LastModifiedAt) >= '2022-10-31' ) 
	AND EXISTS (SELECT TOP (1) hdct.HopDongChiTietID FROM dbo.HopDongChiTiet hdct 
					WHERE hdct.HopDongChiTietID = mn.HopDongChiTietREF 
					AND mn.ThanhTienThucChayBanSauCK <> hdct.ThanhTien))
	) --2022-10-31
	AND mn.DeletedStatus = 0

	OPEN MNDuToan_cursor
	FETCH NEXT FROM MNDuToan_cursor INTO @HopDongChiTietID
	WHILE @@FETCH_STATUS = 0
	BEGIN
		DECLARE @TongTienThucChayMuaTruocCK FLOAT = 0, @ThanhTienHopDongChiTiet FLOAT = 0
		
		--PRINT ''
		--NEU TON TAI ThanhTienMuaNgoaiTruocCK <> 0 THI TINH THEO CONG THUC
		/*'=> thi tinh theo cong thuc : Thành tiền bán sau CK = (TCmuaTruocCK/Tổng thành tiền mua trước CK) * Thành tiền HĐ bán sau ck*/
		IF(EXISTS(SELECT TOP 1 mn.ThucChayMuaNgoaiChiTietID 
				FROM dbo.ThucChayMuaNgoaiChiTiet mn
				INNER JOIN dbo.HopDongChiTiet_MuaNgoai hdct ON mn.HopDongChiTietREF = hdct.HopDongChiTietID
				WHERE hdct.ThanhTienSauCKMua = 0 --dutoan sauck = 0
				AND hdct.HopDongChiTietID = @HopDongChiTietID
				AND mn.ThanhTienMuaNgoaiTruocCK <> 0
				AND mn.DeletedStatus = 0
				
		))
		BEGIN
			--print N'NEU TON TAI ThanhTienMuaNgoaiTruocCK <> 0 THI TINH THEO CONG THUC'
			--TONG TIEN THUC CHAY MUA TRUOC CK
			SET @TongTienThucChayMuaTruocCK = ISNULL((SELECT SUM(mn.[ThanhTienMuaNgoaiTruocCK]) FROM dbo.ThucChayMuaNgoaiChiTiet mn 
												WHERE mn.HopDongChiTietREF = @HopDongChiTietID
												AND mn.DeletedStatus = 0),0) 
			IF(@TongTienThucChayMuaTruocCK <> 0)
			BEGIN
				--THANH TIEN HOPDONG CHI TIET
				SET @ThanhTienHopDongChiTiet = ISNULL((SELECT TOP 1 hdct.ThanhTien FROM dbo.HopDongChiTiet hdct WHERE hdct.HopDongChiTietID = @HopDongChiTietID Order By hdct.HopDongChiTietID),0)
				--select @TongTienThucChayMuaTruocCK
				UPDATE mn
					SET mn.ThanhTienThucChayBanSauCK = (mn.[ThanhTienMuaNgoaiTruocCK]/@TongTienThucChayMuaTruocCK)*@ThanhTienHopDongChiTiet
					,  mn.ThanhTienLaiThucChaySauCK = (mn.[ThanhTienMuaNgoaiTruocCK]/@TongTienThucChayMuaTruocCK)*@ThanhTienHopDongChiTiet
				FROM dbo.ThucChayMuaNgoaiChiTiet mn
				INNER JOIN dbo.HopDongChiTiet_MuaNgoai hdct ON mn.HopDongChiTietREF = hdct.HopDongChiTietID
				WHERE hdct.ThanhTienSauCKMua = 0 --dutoan sauck = 0
				AND hdct.HopDongChiTietID = @HopDongChiTietID
				AND mn.DeletedStatus = 0
			END
		END
		--ThanhTienMuaTruocCK =0
		/*'=> ThanhTienTHucChayBan của khoản mục đầu tiên = thanhtienban*/
		ELSE 
		BEGIN
			--print N'ThanhTienMuaTruocCK =0'
			DECLARE @ThucChayMuaNgoaiChiTietID INT
			SET @ThucChayMuaNgoaiChiTietID = (SELECT TOP 1 ThucChayMuaNgoaiChiTietID FROM dbo.ThucChayMuaNgoaiChiTiet
											WHERE HopDongChiTietREF = @HopDongChiTietID AND DeletedStatus = 0 ORDER BY ThucChayMuaNgoaiChiTietID ASC)
			--THANH TIEN HOPDONG CHI TIET
			SET @ThanhTienHopDongChiTiet = ISNULL((SELECT TOP 1 hdct.ThanhTien FROM dbo.HopDongChiTiet hdct WHERE hdct.HopDongChiTietID = @HopDongChiTietID Order By hdct.HopDongChiTietID),0)
			--cap nhap gia tri ve = 0
			--select @TongTienThucChayMuaTruocCK
			--TAM THOI COMMENT LẠI ĐE SUY NGHI SAU HAIDH 2022-10-31
			--UPDATE mn
			--	SET mn.ThanhTienThucChayBanSauCK = (mn.[ThanhTienMuaNgoaiTruocCK]/@TongTienThucChayMuaTruocCK)*@ThanhTienHopDongChiTiet
			--	,  mn.ThanhTienLaiThucChaySauCK = (mn.[ThanhTienMuaNgoaiTruocCK]/@TongTienThucChayMuaTruocCK)*@ThanhTienHopDongChiTiet
			--FROM dbo.ThucChayMuaNgoaiChiTiet mn
			--INNER JOIN dbo.HopDongChiTiet_MuaNgoai hdct ON mn.HopDongChiTietREF = hdct.HopDongChiTietID
			--WHERE hdct.ThanhTienSauCKMua = 0 --dutoan sauck = 0
			--AND hdct.HopDongChiTietID = @HopDongChiTietID
			--AND mn.DeletedStatus = 0

			--cap nhap gia tri dau tien = thanhtienbansauck
			--select @ThucChayMuaNgoaiChiTietID
			--select @HopDongChiTietID
			--select @ThanhTienHopDongChiTiet
			--select @ThucChayMuaNgoaiChiTietID

			UPDATE dbo.ThucChayMuaNgoaiChiTiet
			SET  ThanhTienThucChayBanSauCK = @ThanhTienHopDongChiTiet
			, ThanhTienLaiThucChaySauCK = @ThanhTienHopDongChiTiet
			WHERE HopDongChiTietREF = @HopDongChiTietID
			AND ThucChayMuaNgoaiChiTietID = @ThucChayMuaNgoaiChiTietID
			AND DeletedStatus = 0
		END
		
		FETCH NEXT FROM MNDuToan_cursor INTO @HopDongChiTietID
	END
	
	CLOSE MNDuToan_cursor
	DEALLOCATE MNDuToan_cursor

END

```
