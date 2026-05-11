# Stored Procedure: `ThucChay_GetTotalValueBaoCaoLechTreoHa`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-01 12:09:58.647000
- **Ngày sửa cuối**: 2014-11-19 12:16:54.957000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@ListDmSanPhamREF` | `nvarchar(400)` | No |
| `@ListSoHopDong` | `nvarchar(4000)` | No |
| `@ListTenNhanVien` | `nvarchar(4000)` | No |
| `@TenDangNhap` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChay_GetTotalValueBaoCaoLechTreoHa] 
	@StartDate DATETIME,
	@EndDate DATETIME,
	@ListDmSanPhamREF NVARCHAR(200),
	@ListSoHopDong NVARCHAR(2000),
	@ListTenNhanVien NVARCHAR(2000),
	@TenDangNhap NVARCHAR(50)
AS
BEGIN
	DECLARE @Sql NVARCHAR(4000)
	DECLARE @DauNhay NVARCHAR(50)
	DECLARE @FillterBySanPham NVARCHAR(200)
	
	DECLARE @GroupPermission INT;
	DECLARE @PhongID INT, @BoPhanID INT, @NhomLamViecID INT, @ChucDanhID INT
	DECLARE @TuNgay DATETIME, @DenNgay DATETIME	
	DECLARE @MinDate DATETIME, @MaxDate DATETIME
	DECLARE @SqlCommand varchar(MAX)
	DECLARE @Count int
	DECLARE @QuaTrinhCongTacTemp TABLE
	(
	  NhanSuID int, 
	  PhongBanREF INT,
	  BoPhanREF INT,
	  NhomLamViecREF INT,
	  ChucDanhREF INT,
	  TuNgay DATETIME,
	  DenNgay DATETIME
	)
	DECLARE @ToUserName NVARCHAR(50)
	
    SET @DauNhay = '''';
    SET @GroupPermission = dbo.NhanSuCheckGroupPermisstion(@TenDangNhap)
    
    SET @ToUserName = (SELECT ToUserName FROM MappingUser A WHERE A.FromUserName = @TenDangNhap)
	
	IF @ToUserName IS NOT NULL
		SET @TenDangNhap = @ToUserName 
	
	SET @SqlCommand = dbo.Fn_GetQuaTrinhCongTacByNhanVien(@TenDangNhap,@StartDate,@EndDate)
	--PRINT @SqlCommand
	
	INSERT INTO @QuaTrinhCongTacTemp(NhanSuID, PhongBanREF, BoPhanREF, NhomLamViecREF, ChucDanhREF, TuNgay, DenNgay)
	EXEC (@SqlCommand)
	
	
	-- Cho Log action nguoi dung
	DECLARE @LogTime						DATETIME
			,@TenBaoCao						NVARCHAR(512)
			,@DmWebsiteREFList				NVARCHAR(50) = ''
			,@DmPhongBanREFList				NVARCHAR(2000) = ''
			,@DmBoPhanREFList				NVARCHAR(2000) = ''
			,@DmNhomLamViecREFList			NVARCHAR(2000) = ''
			,@TenNhanVienList				NVARCHAR(2000) = ''
			,@DmHinhThucQuangCaoList		NVARCHAR(2000) = ''
			,@DmBannerREFList				NVARCHAR(2000) = ''
			,@KhachHangREF					NVARCHAR(512)  = ''
			,@NhanHang						NVARCHAR(4000) = ''
			,@DmNhomNganhREF				NVARCHAR(2000) = ''
			,@TongViewThucChayNoiBo			BIGINT
			,@TongClickThucChayNoiBo		BIGINT
			,@TongSoBaiVietNoiBo			BIGINT
			,@TongSoNgayChayNoiBo			BIGINT
			,@TongViewThucChayKhuyenMai		BIGINT
			,@TongClickThucChayKhuyenMai	BIGINT
			,@TongSoBaiVietKhuyenMai		BIGINT
			,@TongSoNgayChayKhuyenMai		BIGINT
			,@TongViewThucChay				BIGINT
			,@TongClickThucChay				BIGINT
			,@TongSoBaiViet					BIGINT
			,@TongSoNgayChay				BIGINT
			,@TongTienKhuyemMai				FLOAT
			,@TongTienNoiBo					FLOAT
			,@TongTienThucChaySauCK			FLOAT
			,@TongGiaTriThayDoi				FLOAT
			,@IsPheDuyet					INT				= 0
			,@PheDuyetAt					DATETIME
			,@PheDuyetBy					NVARCHAR(50)
			
	SET @TenBaoCao = N'Báo cáo thực chạy lệch treo hạ CPM'
		
	-- Lay So luong theo don vi tinh Click
	SELECT  @TongClickThucChayNoiBo		= 0,
			@TongClickThucChayKhuyenMai = 0,
			@TongClickThucChay			= 0,
			
			@TongViewThucChayNoiBo		= 0,
			@TongViewThucChayKhuyenMai  = 0,
			@TongViewThucChay			= 0,
			
			@TongSoNgayChayNoiBo		= 0,
			@TongSoNgayChayKhuyenMai	= 0,
			@TongSoNgayChay				= 0,
			
			@TongSoBaiVietNoiBo		= 0,
			@TongSoBaiVietKhuyenMai = 0,
			@TongSoBaiViet			= 0
	
	-- Lay Thanh tien thuc chay
	SELECT  
			@TongTienNoiBo				= 0,
			@TongTienKhuyemMai			= 0,
			@TongTienThucChaySauCK		= 0,
			@TongGiaTriThayDoi			= 0

	
	SET @LogTime = GETDATE();
	
	-- Insert action log
	EXEC dbo.LogUserActionFromThucChay_InsertActionLog
		@TenDangNhap
		,@LogTime
		,@TenBaoCao
		,@StartDate
		,@EndDate
		,@ListSoHopDong
		,@DmPhongBanREFList
		,@DmBoPhanREFList
		,@DmNhomLamViecREFList
		,@TenNhanVienList
		,@KhachHangREF
		,@NhanHang
		,@DmNhomNganhREF
		,@DmHinhThucQuangCaoList
		,@ListDmSanPhamREF
		,@DmBannerREFList
		,@DmWebsiteREFList
		,@TongViewThucChayNoiBo
		,@TongClickThucChayNoiBo
		,@TongSoBaiVietNoiBo
		,@TongSoNgayChayNoiBo
		,@TongViewThucChayKhuyenMai
		,@TongClickThucChayKhuyenMai
		,@TongSoBaiVietKhuyenMai
		,@TongSoNgayChayKhuyenMai
		,@TongViewThucChay
		,@TongClickThucChay
		,@TongSoBaiViet
		,@TongSoNgayChay
		,@TongTienKhuyemMai
		,@TongTienNoiBo
		,@TongTienThucChaySauCK
		,@TongGiaTriThayDoi
		,@IsPheDuyet
		,@PheDuyetAt
		,@PheDuyetBy
		
	-- End Insert action log
	PRINT 'OK'

	SET @Count = (SELECT COUNT(*) FROM @QuaTrinhCongTacTemp)
	
	IF @Count <= 1
	BEGIN
		SET @Sql = '
		SELECT 
			CONVERT(BIGINT,SUM(T.TongViewHopDong)) AS TongViewHopDong
			,CONVERT(BIGINT,SUM(T.TongViewThucChay)) AS TongViewThucChay
			,CONVERT(BIGINT,SUM(T.TongViewLechTreoHa)) AS TongViewLechTreoHa
			,ROUND(SUM(T.ThanhTienThucChay),0) AS ThanhTienThucChay
			,ROUND(SUM(T.ThanhTienLechTreoHa),0) AS ThanhTienLechTreoHa
		FROM
		(
			SELECT 
				T1.TenDangNhap, T1.TenNhanVien, T1.SoHopDong
				,CONVERT(BIGINT,MAX(T1.TongViewHopDong)) AS TongViewHopDong
				,CONVERT(BIGINT,SUM(T1.TongViewThucChay)) AS TongViewThucChay
				,CONVERT(BIGINT,SUM(T1.TongViewLechTreoHa)) AS TongViewLechTreoHa
				,ROUND(SUM(T1.ThanhTienThucChay),0) AS ThanhTienThucChay
				,ROUND(SUM(T1.ThanhTienLechTreoHa),0) AS ThanhTienLechTreoHa
				,ROW_NUMBER() OVER (ORDER BY SUM(T1.ThanhTienThucChay) DESC) AS num
			FROM
			('
				+ dbo.ThucChay_GenSQLCommandBaoCaoLechTreoHa(@StartDate,
															 @EndDate,
															 @ListDmSanPhamREF,
															 @ListSoHopDong,
															 @ListTenNhanVien,
															 @TenDangNhap,
															 @PhongID,
															 @BoPhanID,
															 @NhomLamViecID,
															 @ChucDanhID
															) + 
			')T1
			GROUP BY T1.TenDangNhap, T1.TenNhanVien, T1.SoHopDong     
		)T'
			
		--PRINT @Sql
		EXEC (@Sql)
	END
	ELSE
    BEGIN
		DECLARE  @NhomID int
			
		DECLARE @TableResult TABLE
		(
			TenDangNhap nvarchar(50),
			TenNhanVien nvarchar(50),
			SoHopDong NVARCHAR(50),
			TongViewHopDong BIGINT,
			TongViewThucChay BIGINT,
			TongViewLechTreoHa BIGINT,
			ThanhTienThucChay FLOAT,
			ThanhTienLechTreoHa FLOAT,
			RowNumber int
		)
		
		DECLARE Data CURSOR FOR		
			SELECT NhanSuID FROM @QuaTrinhCongTacTemp
			
		OPEN Data;
		DECLARE @CurrentID INT		
		FETCH NEXT FROM Data INTO @CurrentID;
		WHILE @@FETCH_STATUS = 0
		   BEGIN
	   			--SELECT * FROM @TableTemp WHERE ID = @CurrentID   		   			
	   			--PRINT 'CurrentID: ' + CONVERT(nvarchar(50), @CurrentID)	
	   			SET @PhongID = (SELECT PhongBanREF FROM @QuaTrinhCongTacTemp WHERE NhanSuID = @CurrentID)
	   			SET @BoPhanID = (SELECT BoPhanREF FROM @QuaTrinhCongTacTemp WHERE NhanSuID = @CurrentID)
	   			SET @NhomLamViecID = (SELECT NhomLamViecREF FROM @QuaTrinhCongTacTemp WHERE NhanSuID = @CurrentID)
	   			SET @TuNgay = (SELECT TuNgay FROM @QuaTrinhCongTacTemp WHERE NhanSuID = @CurrentID)
	   			SET @DenNgay = (SELECT DenNgay FROM @QuaTrinhCongTacTemp WHERE NhanSuID = @CurrentID)
	   			SET @ChucDanhID = (SELECT ChucDanhREF FROM @QuaTrinhCongTacTemp WHERE NhanSuID = @CurrentID)
	   			
	   			IF @TuNgay < @StartDate
	   				SET @TuNgay = @StartDate
	   				
	   			IF @DenNgay > @EndDate
	   				SET @DenNgay = @EndDate	 
	   			
	   			SET @Sql = '
	   				SELECT 
						T1.TenDangNhap, T1.TenNhanVien, T1.SoHopDong
						,CONVERT(BIGINT,SUM(T1.TongViewHopDong)) AS TongViewHopDong
						,CONVERT(BIGINT,SUM(T1.TongViewThucChay)) AS TongViewThucChay
						,CONVERT(BIGINT,SUM(T1.TongViewLechTreoHa)) AS TongViewLechTreoHa
						,ROUND(SUM(T1.ThanhTienThucChay),0) AS ThanhTienThucChay
						,ROUND(SUM(T1.ThanhTienLechTreoHa),0) AS ThanhTienLechTreoHa
						,ROW_NUMBER() OVER (ORDER BY T1.TenNhanVien) AS num
					FROM
					('
						+ dbo.ThucChay_GenSQLCommandBaoCaoLechTreoHa(@TuNgay,
																	 @DenNgay,
																	 @ListDmSanPhamREF,
																	 @ListSoHopDong,
																	 @ListTenNhanVien,
																	 @TenDangNhap,
																	 @PhongID,
																	 @BoPhanID,
																	 @NhomLamViecID,
																	 @ChucDanhID
																	) + 
					')T1
					GROUP BY T1.TenDangNhap, T1.TenNhanVien, T1.SoHopDong
	   			'
	   			--PRINT @Sql
	   			INSERT INTO @TableResult(TenDangNhap , 
	   									TenNhanVien,
	   									SoHopDong,
	   									TongViewHopDong,
	   									TongViewThucChay ,
	   									TongViewLechTreoHa,
	   									ThanhTienThucChay,
	   									ThanhTienLechTreoHa,
	   									RowNumber)
	   			EXEC (@Sql)
	   						
				FETCH NEXT FROM Data INTO @CurrentID;		  
		   END;	   
		CLOSE Data;
		DEALLOCATE Data;
		
		SELECT 
			T.TongViewHopDong,T.TongViewThucChay,T.TongViewLechTreoHa,
			T.ThanhTienThucChay,T.ThanhTienLechTreoHa
		FROM
		(
			SELECT 
				CONVERT(BIGINT,SUM(T1.TongViewHopDong)) AS TongViewHopDong,
				CONVERT(BIGINT,SUM(T1.TongViewThucChay)) AS TongViewThucChay,
				CONVERT(BIGINT,SUM(T1.TongViewLechTreoHa)) AS TongViewLechTreoHa,
				SUM(T1.ThanhTienThucChay) AS ThanhTienThucChay,
				SUM(T1.ThanhTienLechTreoHa) AS ThanhTienLechTreoHa
			FROM @TableResult T1 
		)T
		
		--PRINT @Sql;

    END
END

```
